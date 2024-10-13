from prefect import flow


from tasks.task_extract_products import task_extract_products
from tasks.task_load_products import task_load_products_baseline, task_load_products_update

TYPE_TASK = "update"  # Cambia a "baseline" según sea necesario

@flow(name="ETL Productos Amazon")
def main_flow():
    search_queries = ["mouse verticale", "hyperx"]
    for query in search_queries:
        products = task_extract_products(query)

        # Obtener el resultado de la tarea
        products_result = products.result()  # Esto se necesita para obtener los resultados

        # Decidir si se realiza una carga inicial o una actualización
        if TYPE_TASK == "baseline":
            task_load_products_baseline(products_result)
        elif TYPE_TASK == "update":
            task_load_products_update(products_result)

# Solo ejecutamos el main_flow si el archivo se llama como archivo principal
if __name__ == "__main__":
    main_flow()