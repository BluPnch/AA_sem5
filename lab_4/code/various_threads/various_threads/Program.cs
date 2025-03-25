using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text.RegularExpressions;
using System.Threading;

namespace lab_4_AA
{
    internal class Program
    {
        private static readonly HttpClient httpClient = new HttpClient();
        private static readonly ConcurrentDictionary<string, bool> visited_addresses = new ConcurrentDictionary<string, bool>();
        private static readonly ConcurrentQueue<string> address_queue = new ConcurrentQueue<string>();
        private static readonly object lockObj = new object();

        static void Main()
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            // string start_address = "https://maguro-tuna.ru/recipes/";
            string start_address = "https://bonduelle.ru/recipes";
            int max_pages = 10;

            Console.WriteLine($"Адрес главной страницы: {start_address}\n");

            int[] threadCounts = { 0, 1, 2, 4, 8, 16, 32 };

            foreach (var threadCount in threadCounts)
            {
                Console.WriteLine($"\nРежим: {(threadCount == 0 ? "Последовательный" : $"Параллельный с {threadCount} потоками")}");

                double averageTime = MeasureExecutionTime(threadCount, start_address, max_pages, 7);
                Console.WriteLine($"Среднее время выполнения: {averageTime} мс");
            }
        }

        private static double MeasureExecutionTime(int threadCount, string start_address, int max_pages, int runs)
        {
            var executionTimes = new List<long>();

            for (int i = 0; i < runs; i++)
            {
                visited_addresses.Clear();
                address_queue.Clear();
                address_queue.Enqueue(start_address);

                var sw = System.Diagnostics.Stopwatch.StartNew();

                if (threadCount == 0)
                    SequentialDischarge(start_address, max_pages);
                else
                    ParallelDischarge(start_address, max_pages, threadCount);

                sw.Stop();
                executionTimes.Add(sw.ElapsedMilliseconds);
            }

            return executionTimes.Average();
        }

        private static void SequentialDischarge(string start_address, int max_pages)
        {
            while (address_queue.TryDequeue(out string current_address) && visited_addresses.Count < max_pages)
            {
                if (!visited_addresses.ContainsKey(current_address))
                    ProcessPage(current_address);
            }
        }

        private static void ParallelDischarge(string start_address, int max_pages, int max_threads)
        {
            var threads = new Thread[max_threads];
            int totalProcessedPages = 0;

            for (int i = 0; i < max_threads; i++)
            {
                threads[i] = new Thread(threadIndex =>
                {
                    int threadIndexInt = (int)threadIndex;
                    int pagesProcessed = 0;

                    while (true)
                    {
                        if (address_queue.TryDequeue(out string current_address))
                        {
                            if (!visited_addresses.ContainsKey(current_address))
                            {
                                ProcessPage(current_address);
                                pagesProcessed++;

                                lock (lockObj)
                                {
                                    visited_addresses[current_address] = true;
                                    totalProcessedPages++;
                                    if (totalProcessedPages >= max_pages)
                                        break;
                                }
                            }
                        }
                        else
                        {
                            Thread.Sleep(100); // Ожидание новых адресов
                        }

                        if (totalProcessedPages >= max_pages)
                            break;
                    }
                });

                threads[i].Start(i);
            }

            foreach (var thread in threads)
            {
                thread.Join(); // Ждем завершения всех потоков
            }
        }


        private static void ProcessPage(string address)
        {
            try
            {
                string page_content = httpClient.GetStringAsync(address).Result;

                SavePageToFile(address, page_content);

                var links = ExtractLinks(page_content);
                foreach (var link in links)
                {
                    if (!visited_addresses.ContainsKey(link))
                        address_queue.Enqueue(link);
                }

                visited_addresses[address] = true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка обработки адреса {address}: {ex.Message}");
            }
        }

        private static void SavePageToFile(string address, string content)
        {
            lock (lockObj)
            {
                string fileName = $"page_{visited_addresses.Count + 1}.html";
                File.WriteAllText(fileName, content);
            }
        }

        private static IEnumerable<string> ExtractLinks(string page_content)
        {
            var links = new List<string>();
            var matches = Regex.Matches(page_content, @"href=""(/recipes/[^""]+)""");
            foreach (Match match in matches)
            {
                if (match.Groups.Count > 1)
                {
                    string link = match.Groups[1].Value;
                    link = "https://maguro-tuna.ru" + link;
                    if (link.Contains("/recipes/"))
                        links.Add(link);
                }
            }
            return links;
        }
    }
}
