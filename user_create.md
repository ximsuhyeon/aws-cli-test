aws iam create-user /
  --user-name Bob

## error
aws.exe: [ERROR]: argument operation: Found invalid choice 'create-'


usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:
  aws help
  aws <command> help
  aws <command> <subcommand> help

    aws iam create-user `
  --user-name Bob

## user to group
    aws iam add-user-to-group `
      --user-name Bob `
      --group-name Admins
