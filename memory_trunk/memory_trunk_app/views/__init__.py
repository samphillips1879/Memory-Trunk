# Landing Page
from .index_view import IndexView

# Auth views
from .register_user_view import UserRegistration
from .register_user_view import register_user
from .login_views import login_user, logout_user, LoginUserView

# Memory views
from .hippocampus_view import hippocampus_view
from .memory_list_view import MemoryListView, PublicMemoryListView
from .memory_detail_view import MemoryDetailView, dislike_memory, like_memory
from .delete_memory_view import delete_memory
from .update_memory_view import update_memory
from .liked_memories_view import LikedMemoriesView

# Tip views
from .tip_creation_view import tip_creation_view
from .tip_list_view import TipListView, PublicTipListView
from .tip_detail_view import TipDetailView, like_tip, dislike_tip
from .delete_tip_view import delete_tip
from .update_tip_view import update_tip
from .liked_tips_view import LikedTipsView

# Perspective views
from .perspective_creation_view import perspective_creation_view
from .perspective_list_view import PerspectiveListView, PublicPerspectiveListView
from .perspective_detail_view import PerspectiveDetailView, like_perspective, dislike_perspective
from .delete_perspective_view import delete_perspective
from .update_perspective_view import update_perspective
from .liked_perspectives_view import LikedPerspectivesView

# Search
from .model_search_view import search

# Happy Memory
from .happy_memory import happy_memory