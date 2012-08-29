import sys
import os

from clint import args
from clint.textui import colored, puts, indent

from .core import delete_gist, create_gist
from .config import login, make_config, write_config, config_file


def show_help():
    puts('{0}. Created by Olaoluwa Osuntokun'.format(
        colored.blue('pygist')))

    with indent(4):
        puts(colored.green('pygist login'))
        puts(colored.green('pygist create <file1> <file2> <fileN> "description"'))
        puts(colored.green('pygist create paste "description"'))
        puts(colored.green('pygist delete <gist_id>'))
        puts('\n')


def begin():
    if os.path.exists(config_file):
        pass
    else:
        #make config file
        make_config()
        write_config()

    if args.get(0) is None:
        show_help()

    elif args.flags.contains(('--help', '-h')) or args.get(0) == 'help':
        show_help()
        sys.exit(0)

    elif args.flags.contains(('--login', '-l')) or args.get(0) == 'login':
        username = args.get(1)
        if username is None:
            username = raw_input("Github username: ")
            if len(username) == 0:
                puts("{0}. {1}".format(
                    colored.blue("pygist"),
                    colored.red("Username was blank")))

        password = args.get(2)
        if password is None:
            import getpass
            password = getpass.getpass("Password: ")

        login(username, password)

    elif args.get(0) == 'delete':
        if args.get(1) is None:
            puts('{0}. {1}'.format(colored.blue('pygist'),
                 colored.red('You need to pass a gist number to delete')))
        else:
            gist_id = args.get(1)
            delete_gist(gist_id)

    elif args.get(0) == 'create':
        if args.get(1) == 'paste':
            description = args.get(2) or ''
            create_gist(paste=True, description=description)
        elif not args.files:
            puts('{0}. {1}'.format(colored.blue('pygist'),
                 colored.red('You need to pass file as well to create a gist')))
        else:
            description = args.not_files.get(1) or ''
            files = args.files
            create_gist(files=files, description=description)

    else:
        show_help()
        sys.exit(0)
