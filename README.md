# breathOS

Beatiful, secure, and transparent OS with with a focus on UX design and build reproducibility.

The current Linux desktop caters to the "1%" of developers. Most users will never crack-open the command-line. Installation of applications and updates of the OS should be seamless and foregettable, like with the original iPhone vision.

And current beautifully designed OS, like MacOS, disregards the developer. Making it closed source and gate-keeping the developer.

All current mainline OS suffer from the lack of reproducibility. Yet the OS communities that heroicly got us reproducible systems, such as NixOS, are totally user unfriendly and app developer unfriendly.

We prepose a balance. NixOS (Nix-like) system with userland container applications. Nix-like system community can do what it does best, creating reproducible builds and configurations. And developers can do what they do best, create applications that users need and love.

The following are an intrepretation of these requirements.

## System Updates

- All updates happen via nix-pkgs, or similar package manager.
- Ability for the system to rollback (only the system can do so).

There is no "package manager" in the conventional sense of the word.

## System Manager

All configurations securely made here. Under the hood, its configured using Nix flakes.

## App Collection

A curated collection of containerized applications by the community. The ratings and rankings are transparent that prevent fake users participation and spam feedback.

Installations are point and click. Users can rollback the applications to any state (future may be some limitations for security reasons).

- Dockerfile
- Docker-compose
- git

Developers create an `app.collection` file. It is simply a json file:

```
{
   ContributorID: <>,
   gitURL: <>,
}
```

Any change in this file makes it another app. The has, signed with ContributorID, is the AppID.

`App Collection` will build the Docker image after cloning the repo. App Collection will check for latest master commits. If there are some it doesn't have, it tells the user an update is available. One-click fires of the reinstallation (the update).

All App Collection git repos must conform to the following format to build successfully:

- A directory called `.breathOS/`, with an `app.collection` file

- A `app-image/`subdirectory with Dockerfiles. If there is only one Dockerfile, it must be named `app.file`.

- An optional a `app.manager` (a docker-compose) file in the breathOS root folder.