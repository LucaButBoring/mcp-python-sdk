from dataclasses import dataclass
from typing import Any, Generic

from typing_extensions import TypeVar

from mcp.shared.async_operations import BaseOperationManager
from mcp.shared.session import BaseSession
from mcp.types import RequestId, RequestParams

SessionT = TypeVar("SessionT", bound=BaseSession[Any, Any, Any, Any, Any])
OperationManagerT = TypeVar("OperationManagerT", bound=BaseOperationManager[Any])
LifespanContextT = TypeVar("LifespanContextT")
RequestT = TypeVar("RequestT", default=Any)


@dataclass
class RequestContext(Generic[SessionT, OperationManagerT, LifespanContextT, RequestT]):
    request_id: RequestId
    operation_manager: OperationManagerT
    operation_token: str | None
    meta: RequestParams.Meta | None
    session: SessionT
    lifespan_context: LifespanContextT
    request: RequestT | None = None
