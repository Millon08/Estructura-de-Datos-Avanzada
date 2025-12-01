using System;
using System.Collections.Generic;
using System.IO;

namespace GrafoActividad
{
    public class Arista
    {
        public string Origen { get; set; }
        public string Destino { get; set; }
        public int Peso { get; set; }

        public Arista(string origen, string destino, int peso)
        {
            Origen = origen;
            Destino = destino;
            Peso = peso;
        }
    }

    class Program
    {
        static List<Arista> grafo = new List<Arista>();
        static bool esDirigido = false; 

        static void Main(string[] args)
        {
            grafo.Clear();

            Console.WriteLine("--- Generando Grafo ---");
            Console.WriteLine($"Modo: {(esDirigido ? "Dirigido" : "No Dirigido")}");

            AgregarConexion("Casa", "Parque", 5);
            AgregarConexion("Casa", "Supermercado", 10);
            AgregarConexion("Parque", "Escuela", 8);
            AgregarConexion("Supermercado", "Escuela", 4);
            AgregarConexion("Supermercado", "Cine", 6);
            AgregarConexion("Escuela", "Hospital", 15);
            AgregarConexion("Cine", "Hospital", 2);

            EliminarConexion("Supermercado", "Cine");

            GenerarArchivo();
        }

        static void AgregarConexion(string origen, string destino, int peso)
        {
            grafo.Add(new Arista(origen, destino, peso));
            
            if (!esDirigido)
            {
                grafo.Add(new Arista(destino, origen, peso));
            }
        }

        static void EliminarConexion(string origen, string destino)
        {
            grafo.RemoveAll(a => a.Origen == origen && a.Destino == destino);

            if (!esDirigido)
            {
                grafo.RemoveAll(a => a.Origen == destino && a.Destino == origen);
            }
        }

        static void GenerarArchivo()
        {
            string rutaArchivo = "edges.txt";
            try 
            {
                using (StreamWriter sw = new StreamWriter(rutaArchivo))
                {
                    foreach (var arista in grafo)
                    {
                        sw.WriteLine($"{arista.Origen},{arista.Destino},{arista.Peso}");
                    }
                }
                Console.WriteLine($"Archivo {rutaArchivo} actualizado exitosamente.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
        }
    }
}