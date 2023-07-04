# breathOS

Experience a beautiful, secure, and transparent operating system that embodies a unique balance between UX design and build reproducibility.

Too often, existing Linux desktop environments cater only to the upper echelon of developers, leaving the majority who seldom utilize the command-line in the lurch. Meanwhile, elegantly designed OS like MacOS, despite their aesthetic appeal, limit developers by being closed-source.

What's more, many mainstream operating systems grapple with the problem of reproducibility. While some OS communities such as NixOS have made strides towards creating reproducible systems, these solutions tend to be unfriendly for users and application developers alike.

Enter breathOS—a harmonious blend of a Nix-like system and user-friendly, containerized applications. In this milieu, the Nix community excels at doing what it does best: crafting reproducible builds and configurations. Concurrently, developers focus on their strength: creating applications that meet user needs and are loved by all.

Here's a closer look at the key features and principles underpinning breathOS.

## System Updates

- Updates are delivered via nix-pkgs or a similar package manager, making the conventional concept of a "package manager" redundant.
- The system reserves the exclusive ability to rollback.

## System Manager

All configurations are securely handled via the System Manager. While this may be underpinned by Nix flakes, users won't need to delve under the hood.

## App Collection

The App Collection is a curated assortment of containerized applications contributed by the community. The transparent rating and ranking system prevents fraudulent user participation and spam feedback. Installation is as simple as a point-and-click action, with the ability for users to rollback applications to any state, although certain future limitations may apply for security reasons.

### Contributing to the App Collection

Developers contribute by creating an `app.collection` file, a straightforward JSON file:

```
{
   ContributorID: <>,
   gitURL: <>,
}
```
This file, when altered, creates a distinct app. The hash, signed with the ContributorID, becomes the AppID.

Upon receiving the JSON file, the App Collection clones the repository and builds the Docker image. It then checks for any newer commits on the master branch, notifying the user if an update is available. A single click launches the reinstallation (the update).

### App Collection Repository Format

To successfully build an app, all App Collection git repositories must adhere to the following format:

- A directory named `.breathOS/`, containing an `app.collection` file.
- A subdirectory named `app-image/`, housing Dockerfiles. If there's only one Dockerfile, it must be named `app.file`.
- Optionally, an `app.manager` file (a docker-compose file) located in the breathOS root folder.
