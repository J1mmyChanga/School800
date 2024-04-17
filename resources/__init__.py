from .login import LoginResource
from .register import RegisterResource
from .tasks import TaskResource, TasksListResource, TasksPunishmentResource
from .groups import GroupResource, GroupPhotoResource
from .kinds import KindsListResource
from .users import UserResource, UserPhotoResource, UsersListResource, AddingUserPhotoResource, MVUsersInGroup, MVUsers
from .tasks_to_user import CompletedTasksResource, InProcessTasksResource, UndoneTasksResource
from .tasks_photo import TaskPhotoResource, AddingTaskPhotoResource
from .tasks_completed_photo import CompletedTaskPhotoResource, AddingCompletedTaskPhotoResource