import base

from datetime import datetime

class TimeStampMixin(base.Base):
    created_at = base.Column(base.DateTime, default=datetime.now())
    updated_at = base.Column(base.DateTime, default=datetime.now(), onupdate=datetime.now())
