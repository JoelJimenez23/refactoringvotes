import csv
from typing import Dict, Tuple

def read_votes(file_path: str) -> Dict[str, int]:
    """
    Lee los votos de un archivo csv y retorna un diccionario con el total de votos por candidato

    Extraccion de metodos: Se creo un metodo especifico para leer el archivo csv y acumular los votos
    """
    results = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Saltar el encabezado

        for row in reader:
            city, candidate, votes = parse_row(row)
            # Eliminación de código duplicado: Usamos `get` para evitar un bloque `if-else`
            results[candidate] = results.get(candidate, 0) + votes

    return results

def parse_row(row: list) -> Tuple[str, str, int]:
    """
    Convierte una fila del archivo CSV en datos utilizables.
    
    - Extraccion de metodos: Se creo un metodo especifico para procesar una fila
    - Simplificacion de condicionales: Maneja errores de conversion de forma especifica con `ValueError`
    """
    city = row[0]
    candidate = row[1]
    try:
        votes = int(row[2])
    except ValueError:
        votes = 0
    return city, candidate, votes

def display_results(results: Dict[str, int]) -> None:
    """
    Muestra el total de votos por candidato y el ganador.
    
    Extraccion de metodos: Se creo un metodo para mostrar los resultados y el ganador.
    """
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

    winner = find_winner(results)
    print(f"winner is {winner}")

def find_winner(results: Dict[str, int]) -> str:
    """
    Encuentra el candidato con el mayor número de votos.
    Retorna 'Tie' si hay un empate entre los candidatos con el mayor numero de votos.
    """
    sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    max_votes = sorted_results[0][1]
    
    # Verificamos si más de un candidato tiene el número máximo de votos
    top_candidates = [candidate for candidate, votes in sorted_results if votes == max_votes]
    if len(top_candidates) > 1:
        return "Tie"
    return top_candidates[0]


def count_votes(file_path: str) -> None:
    """
    Funcion principal que lee los votos, muestra los resultados y el ganador.
    Division de metodos grandes: Separar la logica en funciones pequeñas y especificas.
    Modularidad: Hace que el codigo sea facil de leer y probar cada componente por separado.
    """
    results = read_votes(file_path)
    display_results(results)

# Ejemplo de uso
count_votes('votes.csv')
