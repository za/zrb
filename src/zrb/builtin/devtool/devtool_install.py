from .helper import create_installer
from ...task_input.str_input import StrInput
from ...task_input.bool_input import BoolInput
from ...runner import runner

# GVM
gvm_install_task = create_installer(
    name='gvm',
    description='GVM provides interface to manage go version',
    inputs=[
        StrInput(
            name='go-default-version',
            description='Go default version',
            default='go1.14'
        )
    ],
    config_locations=['~/.bashrc', '~/.zshrc']
)
runner.register(gvm_install_task)

# PyEnv
pyenv_install_task = create_installer(
    name='pyenv',
    description='Simple Python version management',
    inputs=[
        StrInput(
            name='python-default-version',
            description='Python default version',
            default='3.9.0'
        )
    ],
    config_locations=['~/.bashrc', '~/.zshrc']
)
runner.register(pyenv_install_task)

# NVM
nvm_install_task = create_installer(
    name='nvm',
    description=' '.join([
        'NVM allows you to quickly install and use different versions',
        'of node via the command line'
    ]),
    inputs=[
        StrInput(
            name='node-default-version',
            description='Node default version',
            default='node'
        )
    ],
    config_locations=['~/.bashrc', '~/.zshrc']
)
runner.register(nvm_install_task)

# sdkman
sdkman_install_task = create_installer(
    name='sdkman',
    description=' '.join([
        'SDKMAN! is a tool for managing parallel versions of multiple',
        'Software Development Kits on most Unix based systems'
    ]),
    inputs=[
        BoolInput(
            name='install-java',
            description='Install Java',
            prompt='Do you want to install Java?',
            default=True
        ),
        BoolInput(
            name='install-scala',
            description='Install Scala',
            prompt='Do you want to install Scala?',
            default=True
        )
    ],
    config_locations=['~/.bashrc', '~/.zshrc']
)
runner.register(sdkman_install_task)

# pulumi
pulumi_install_task = create_installer(
    name='pulumi',
    description='Universal infrastructure as code',
    config_locations=['~/.bashrc', '~/.zshrc']
)
runner.register(pulumi_install_task)

# AWS
aws_install_task = create_installer(
    name='aws',
    description='AWS CLI',
    ask_config_location=False
)
runner.register(aws_install_task)

# GCloud
gcloud_install_task = create_installer(
    name='gcloud',
    description='Gcloud CLI',
    ask_config_location=False
)
runner.register(gcloud_install_task)

# Tmux
tmux_install_task = create_installer(
    name='tmux',
    description='Tmux',
    default_config_location='~/.tmux.conf',
    remove_old_config=True
)
runner.register(tmux_install_task)

# Zsh
zsh_install_task = create_installer(
    name='zsh',
    description='Zsh terminal + oh-my-zsh + zdharma',
    default_config_location='~/.zshrc',
    remove_old_config=True
)
runner.register(zsh_install_task)

# Kubectl
kubectl_install_task = create_installer(
    name='kubectl',
    description='Kubernetes CLI tool',
    ask_config_location=False
)
runner.register(kubectl_install_task)

# Helm
helm_install_task = create_installer(
    name='helm',
    description='Package manager for kubernetes',
    ask_config_location=False
)
runner.register(helm_install_task)

# Terraform
terraform_install_task = create_installer(
    name='terraform',
    description='Open source IAC by Hashicorp',
    config_locations=['~/.bashrc', '~/.zshrc']
)
runner.register(terraform_install_task)

