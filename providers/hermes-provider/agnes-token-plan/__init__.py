"""Agnes AI Token Plan provider profile.

Agnes AI provides an OpenAI-compatible API at:

    https://apihub.agnes-ai.com/v1

This provider targets the Agnes AI Token Plan subscription tier.
It uses the same API endpoint as the Free tier but operates with a
dedicated RPM and quota pool.

For higher capacity production workloads, use this provider instead
of the default Agnes AI Free tier.
"""

from providers import register_provider
from providers.base import ProviderProfile


agnes_token_plan = ProviderProfile(
    name="agnes-token-plan",
    aliases=(
        "agnes_tp",
        "agnes_token_plan",
    ),
    display_name="Agnes AI (Token Plan)",
    description=(
        "Agnes AI Token Plan — OpenAI-compatible multimodal API "
        "with dedicated RPM limits and quota allocation."
    ),
    signup_url="https://platform.agnes-ai.com/",
    env_vars=(
        "AGNES_TOKEN_PLAN_API_KEY",
        "AGNES_BASE_URL",
    ),
    base_url="https://apihub.agnes-ai.com/v1",
    auth_type="api_key",
    default_aux_model="agnes-2.0-flash",
    fallback_models=(
        "agnes-2.0-flash",
    ),
)

register_provider(agnes_token_plan)
