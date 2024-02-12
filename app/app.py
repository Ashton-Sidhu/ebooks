import streamlit as st
from sidhulabs.elastic.client import get_elastic_client
from sidhulabs.elastic.documents import get_all

st.title("Ebook Search")

search = st.text_input("Search through Ebooks")

es_client = get_elastic_client("https://elastic.sidhulabs.ca:443")


if search:

    results = es_client.search(
        index="books",
        query={
            "match": {
                "content": {
                    "query": search, 
                    "operator": "and"
                }
            }
        }
    )

    results = results["hits"]["hits"]

    if not results:
        st.warning("No results found.")

    st.info(f"Found {len(results)} results!")

    for result in results:
        st.write(result["_source"]["title"])
        
        content: str = result["_source"]["content"].lower().  

        st.write(content.index("bidirectional"))
