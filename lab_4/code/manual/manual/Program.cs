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
            string start_address = "https://maguro-tuna.ru/recipes/";
            int max_pages = 100, mode = 2, max_threads = 8;
            Console.WriteLine($"Адрес главной страницы: {start_address}\n");
            

            Console.WriteLine("Введите максимальное количество страниц для возможной обработки: ");
            max_pages = int.Parse(Console.ReadLine());

            Console.WriteLine("Выберите режим: \n 1. Последовательный \n 2. Параллельный");
            mode = int.Parse(Console.ReadLine());

            if (mode == 2)
            {
                Console.WriteLine("Введите максимальное количество потоков: ");
                max_threads = int.Parse(Console.ReadLine());
            }
            
            if (mode == 1) // последовательное
                SequentialDischarge(start_address, max_pages);
            else // параллельное
                ParallelDischarge(start_address, max_pages, max_threads);
        }

        private static void SequentialDischarge(string start_address, int max_pages)
        {
            var sw = System.Diagnostics.Stopwatch.StartNew();
            
            address_queue.Enqueue(start_address);
            while (address_queue.TryDequeue(out string current_address) && visited_addresses.Count < max_pages)
            {
                if (!visited_addresses.ContainsKey(current_address))
                    ProcessPage(current_address);
            }

            sw.Stop();
            
            Console.WriteLine($"Последовательная обработка завершена. Время: {sw.ElapsedMilliseconds} мс");
        }

        private static void ParallelDischarge(string start_address, int max_pages, int max_threads)
        {
            var sw = System.Diagnostics.Stopwatch.StartNew();
            
            address_queue.Enqueue(start_address);
            var threads = new List<Thread>();
            for (int i = 0; i < max_threads; i++)
            {
                var thread = new Thread(() =>
                {
                    while (visited_addresses.Count < max_pages)
                    {
                        if (address_queue.TryDequeue(out string current_address))
                        {
                            if (!visited_addresses.ContainsKey(current_address))
                                ProcessPage(current_address);
                        }
                    }
                });
                
                threads.Add(thread);
                thread.Start();
            }

            foreach (var thread in threads)
                thread.Join();

            sw.Stop();
            
            Console.WriteLine($"Параллельная обработка завершена. Время: {sw.ElapsedMilliseconds} мс");
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
                Console.WriteLine($"Сохранено: {fileName}");
            }
        }

        private static IEnumerable<string> ExtractLinks(string page_content)
        {
            var links = new List<string>();
            var matches = Regex.Matches(page_content, @"href=""(http[s]?://[^""]+)""");

            foreach (Match match in matches)
            {
                if (match.Groups.Count > 1)
                    links.Add(match.Groups[1].Value);
            }

            return links;
        }
    }
}