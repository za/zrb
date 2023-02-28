from ....helper.file.copy_tree import copy_tree
from ....helper.codemod.add_assert_resource import add_assert_resource
from ....helper.codemod.add_import_module import add_import_module
from ....helper.codemod.add_upstream_to_task import add_upstream_to_task

import os

current_dir = os.path.dirname(__file__)


def add_project_automation(project_dir: str):
    if os.path.exists(os.path.join(project_dir, '_automate', '_project')):
        return
    copy_tree(
        src=os.path.join(current_dir, 'template'),
        dst=project_dir
    )
    project_task_module_path = '_automate._project'
    zrb_init_path = os.path.join(project_dir, 'zrb_init.py')
    with open(zrb_init_path, 'r') as f:
        code = f.read()
        import_alias = project_task_module_path.split('.')[-1]
        code = add_import_module(
            code=code,
            module_path=project_task_module_path,
            alias=import_alias
        )
        code = add_assert_resource(code, import_alias)
    with open(zrb_init_path, 'w') as f:
        f.write(code)


def register_project_upstream(
    project_dir: str,
    project_automation_file: str,
    project_automation_task_name: str,
    upstream_task_file: str,
    upstream_task_var: str
):
    '''
    Adding upstream_task_var as project_task's
    '''
    project_automation_dir = os.path.join(
        project_dir, '_automate', '_project'
    )
    project_automation_path = os.path.join(
        project_automation_dir, f'{project_automation_file}'
    )
    upstream_task_rel_file_path = os.path.relpath(
        upstream_task_file, project_automation_path
    )
    # normalize `..` parts
    upstream_module_parts = [
        part if part != '..' else ''
        for part in upstream_task_rel_file_path.split(os.path.sep)
    ]
    # remove .py extenstion
    upstream_module_parts[-1] = os.path.splitext(upstream_module_parts[-1])[0]
    upstream_module_path = '.'.join(upstream_module_parts)
    with open(project_automation_path, 'r') as f:
        code = f.read()
        code = add_import_module(
            code=code,
            module_path=upstream_module_path,
            resource=upstream_task_var
        )
        code = add_upstream_to_task(
            code, project_automation_task_name, upstream_task_var
        )
    with open(project_automation_path, 'w') as f:
        f.write(code)
