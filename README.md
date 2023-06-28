# notion_bck

Creates a Notion backup based on a personal integration.

Reference: https://notionbackups.com/blog/automated-notion-backup-api

### To Do

- In large workspaces, results are more likely to be paginated. To obtain all items, you will have to recursively query the search endpoint until the `has_more` parameter returns `false`.
