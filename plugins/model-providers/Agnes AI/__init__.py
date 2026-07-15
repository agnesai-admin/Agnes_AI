"""Agnes AI provider profile.

Agnes AI, developed by Sapiens AI, provides an OpenAI-compatible
multimodal API for text generation, reasoning, image generation,
image editing, image understanding, and video generation.

Base URL:
    https://apihub.agnes-ai.com/v1

Authentication:
    Authorization: Bearer <AGNES_API_KEY>

Currently supported models:
    Text:
        - agnes-2.0-flash

    Image:
        - agnes-image-2.0-flash
        - agnes-image-2.1-flash

    Video:
        - agnes-video-v2.0

Primary endpoints:
    Text:
        POST /v1/chat/completions

    Image:
        POST /v1/images/generations

    Video:
        POST /v1/videos

Video generation is asynchronous. Results can be retrieved using:
    GET /agnesapi?video_id=<VIDEO_ID>
"""
from providers import register_provider
from providers.base import ProviderProfile


Agnes_AI = ProviderProfile(
    name="Agnes-AI",
    aliases=(
        "Agnes-AI",
        "agnes",
        "agnes_ai",
    ),
    display_name="Agnes AI",
    description=(
        "OpenAI-compatible multimodal AI provider supporting text generation, "
        "reasoning, coding, tool calling, image understanding, image generation, "
        "image editing, and video generation."
    ),
    signup_url="https://platform.agnes-ai.com/",
    env_vars=(
        "AGNES_API_KEY",
        "AGNES_BASE_URL",
    ),
    base_url="https://apihub.agnes-ai.com/v1",
    default_aux_model="agnes-2.0-flash",
)

register_provider(Agnes_AI)
