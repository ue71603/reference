from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class WorkflowStatusEnumeration(Enum):
    DRAFT = "draft"
    PENDING_APPROVAL = "pendingApproval"
    APPROVED_DRAFT = "approvedDraft"
    OPEN = "open"
    PUBLISHED = "published"
    CLOSING = "closing"
    CLOSED = "closed"
