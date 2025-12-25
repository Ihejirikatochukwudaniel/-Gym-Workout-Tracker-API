"""Import all model modules so they are registered on SQLAlchemy metadata."""
from . import user  # noqa: F401
from . import exercise  # noqa: F401
from . import workout  # noqa: F401
from . import template  # noqa: F401
from . import goal  # noqa: F401
