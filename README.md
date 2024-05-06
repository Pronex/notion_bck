# notion_bck

Creates a Notion backup based on a personal integration.

Reference: [link](https://notionbackups.com/blog/automated-notion-backup-api)

## Running the script

Create a config file named `congig.yml` with at least the following content:

```yaml
notion_token: "secret_***"
```

Then run the script with:

```bash
python3 notion_bck.py
```

## To Do

- In large workspaces, results are more likely to be paginated. To obtain all items, you will have to recursively query the search endpoint until the `has_more` parameter returns `false`.
