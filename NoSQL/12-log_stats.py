#!/usr/bin/env python3
"""
task 12
"""
import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    doc_c = collection.estimated_document_count()
    print(f"{doc_c} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    stat_c = collection.count_documents(
            {
                "method": "GET",
                "path": "/status"
            }
        )

    print(f"{stat_c} status check")
