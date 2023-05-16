# LlamaIndex demo

This project provides a very simple but working example of using LlamaIndex to enable natural-language querying of a GitHub repository. It's described in a Medium article I wrote, [Getting started with LlamaIndex](https://medium.com/@ofrasergreen/getting-started-with-llamaindex-169bbf475a94).

# Running the demo

1. Clone this repository
2. Copy the `env.example` file to `.env` and replace the tokens with:
   * A GitHub personal access token generated in the [GitHub settings page](https://github.com/settings/tokens/new). Create a token with `repo`and `read:org` scopes.
   * An OpenAI key generated in the [OpenAI platform page](https://platform.openai.com/account/api-keys).
3. Create a poetry shell and run the code:

```
$ poetry shell
$ python ingest.py
$ python query.py
```
