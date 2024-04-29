# Example of NiceGUI Issue

## Setup

Have PyEnv and Poetry installed globally.

Use Poetry to install dependencies. This should automatically create a virtualenv for this project.

```shell
poetry install
```

Now run the start script in the environment

```shell
poetry run ./run.sh
```

See [this video](./missing-chars.mp4) where the trailing `ost` was lost when typing quickly. When typing slowly this doesn't happen.
