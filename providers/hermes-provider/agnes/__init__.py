"""Agnes AI provider profile.

Agnes AI provides an OpenAI-compatible API for text generation,
reasoning, coding, image understanding, image generation,
image editing, and video generation.

API Base URL:
    https://apihub.agnes-ai.com/v1
"""

from providers import register_provider
from providers.base import ProviderProfile


agnes = ProviderProfile(
    name="agnes",
    aliases=(
        "agnes-ai",
        "agnes_ai",
    ),
    display_name="Agnes AI",
    description=(
        "Agnes AI OpenAI-compatible multimodal API supporting "
        "text generation, reasoning, coding, tool calling, "
        "image generation, image editing, and video generation."
    ),
    signup_url="https://platform.agnes-ai.com/",
    env_vars=(
        "AGNES_API_KEY",
        "AGNES_BASE_URL",
    ),
    base_url="https://apihub.agnes-ai.com/v1",
    auth_type="api_key",
    default_aux_model="agnes-2.0-flash",
    fallback_models=(
        "agnes-2.0-flash",
    ),
)

register_provider(agnes)
