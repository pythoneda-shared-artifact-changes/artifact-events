# Artifact events

Shared kernel for events emitted by artifacts themselves.

# How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-artifact/artifact-events-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-artifact-artifact-events-artifact = {
      [optional follows]
      url =
        "github:pythoneda-shared-artifact/artifact-events-artifact/[version]?dir=artifact-events";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project.
The Nix flake is under the artifact-events folder of https://github.com/pythoneda-shared-artifact/artifact-events-artifact.
