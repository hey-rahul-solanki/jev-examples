# Migrate product catalog search to Elasticsearch

## Context

The product catalog currently uses relational database queries for search. Search performance has deteriorated as the catalog has grown.

## Requirements

- Move product search to Elasticsearch.
- Keep the existing API contract backward compatible.
- Support search by product name, SKU, category and brand.
- Existing filters and sorting should continue to work.
 - Product updates should be reflected in the search index.
 - Search latency should be below 300ms.

## Technical notes

The catalog contains approximately 2 million products. There is currently no Elasticsearch cluster in the environment. We will need to decide on the indexing schema, complete an initial backfill, and keep the index synchronized with product updates.
