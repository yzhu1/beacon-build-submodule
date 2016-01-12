This directory contains build scripts specific to the wgspring webapp stack.
It is intended to be used as a submodule of the main application project.

Most "but it isn't working" failures are the result of not setting all
the required properties in default.build.properties in the parent
project, but some special cases are pretty obscure.  Most notably,

    [javac] warning: [options] bootstrap class path not set in conjunction with -source 1.6

means that the build.source and build.target properties are set for
Java 6, but the JVM that is running ant is (probably) Java 8.  Setting
a "bootstrap path" as indicated in the error message is actually
probably the wrong solution: instead, set the JAVA_HOME environment
variable to a directory such that you are compiling with a Java 6 JDK,
not a Java 8 JDK, and the problem will go away.
