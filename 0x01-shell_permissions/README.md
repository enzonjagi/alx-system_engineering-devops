#0x01-shell_permissions
0-iam_betty changes current user to betty
1-who_am_i lists the effective username of the current user
2-groups prints all the groups the current user is part of.
3-new_owner changes file ownership to betty
4-empty creates an empty file called hello
5-execute changes the mode of the file "hello" to executable
6-multiple_permissions adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7-everybody adds execution permission to the owner, the group owner and the other users, to the file hello
8-James_Bond sets the permission to the file hello as; Owner: no permission at all, Group: no permission at all, Other users: all the permissions.
9-John_Doe sets the mode of the file hello to; "-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello"
10-mirror_permissions Write a script that sets the mode of the file hello the same as olleh
11-directories_permissions adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
