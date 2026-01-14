from concurrent.futures import ThreadPoolExecutor, as_completed

# Number of threads to use for parallel execution
num_threads = len(sql_queries)

def run_parallel_queries(queries):
    results = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_query = {executor.submit(execute_query, query): query for query in queries}
        for future in as_completed(future_to_query):
            query = future_to_query[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                print(f"Query '{query}' generated an exception: {exc}")
    return results

# Run queries in parallel
query_results = run_parallel_queries(sql_queries)

# Optionally, process the results
for result in query_results:
    result.show()






###################################################################################################################



from concurrent.futures import ThreadPoolExecutor, as_completed



from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Parallel SQL Queries") \
    .getOrCreate()


def execute_query(query):
    return spark.sql(query)
    

# Define your SQL queries
queries = [
    "SELECT COUNT(*) FROM table1",
    "SELECT AVG(column1) FROM table2",
    "SELECT * FROM table3 WHERE column2 > 100"
]

# Function to execute SQL queries
def run_query(query):
    try:
        df = execute_query(query)
        return df.collect()  # Or use df.show() to display results
    except Exception as e:
        return str(e)

# Use ThreadPoolExecutor to execute queries in parallel
with ThreadPoolExecutor(max_workers=len(queries)) as executor:
    future_to_query = {executor.submit(run_query, query): query for query in queries}

    for future in as_completed(future_to_query):
        query = future_to_query[future]
        try:
            result = future.result()
            print(f"Results for query '{query}':")
            for row in result:
                print(row)
        except Exception as exc:
            print(f"Query '{query}' generated an exception: {exc}")
