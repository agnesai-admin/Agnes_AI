# Agnes AI

<p align="center">
  <b>OpenAI-Compatible Multimodal AI Provider</b>
</p>

<p align="center">
  Hermes integration for Agnes AI — enabling text, image, video, and multimodal AI capabilities through an OpenAI-compatible API.
</p>

---

## Overview

Agnes AI is a multimodal AI platform developed by **Sapiens AI**.

Agnes AI provides developers with unified AI model services through an OpenAI-compatible API, allowing applications to integrate advanced AI capabilities with minimal changes.

The platform supports:

- Text generation and reasoning
- Coding assistance
- AI agents and workflows
- Image generation and editing
- Video generation
- Multimodal AI applications

Agnes AI is designed to help developers, startups, and enterprises integrate powerful AI capabilities into their products and applications.

---

# API Compatibility

Agnes AI provides an OpenAI-compatible API interface.

Existing OpenAI-compatible applications can connect by configuring:

- API Base URL
- API Key
- Model Name

API Base URL:

```text
https://apihub.agnes-ai.com/v1
```

Authentication:

```http
Authorization: Bearer YOUR_API_KEY
```

---

# Hermes Providers

This repository provides two Agnes AI provider profiles:

```
providers/
└── hermes-provider/
    ├── agnes/
    │   ├── __init__.py
    │   └── plugin.yaml
    │
    └── agnes-token-plan/
        ├── __init__.py
        └── plugin.yaml
```

---

# Providers

## Agnes AI (Free)

The default Agnes AI provider.

Designed for developers using the Free API tier.

Features:

- OpenAI-compatible API access
- Standard quota allocation
- Standard request limits
- Access to Agnes AI models

Environment variables:

```bash
AGNES_API_KEY
AGNES_BASE_URL
```

---

## Agnes AI Token Plan

The Token Plan provider is designed for paid usage-based access.

It uses the same Agnes AI API endpoint but provides a separate subscription tier with dedicated resource allocation.

Features:

- Dedicated quota pool
- Higher request capacity
- Better suitability for production workloads

Environment variables:

```bash
AGNES_TOKEN_PLAN_API_KEY
AGNES_BASE_URL
```

---

# Supported Models

## Text Models

### agnes-2.0-flash

A fast and efficient language model supporting:

- Chat completion
- Reasoning
- Coding assistance
- Tool calling
- Agent workflows
- Image understanding

---

## Image Models

### agnes-image-2.0-flash

Supports:

- Text-to-image generation
- Image editing
- Creative workflows

### agnes-image-2.1-flash

Supports:

- High-detail image generation
- Complex compositions
- Image transformation workflows

---

## Video Models

### agnes-video-v2.0

Supports:

- Text-to-video generation
- Image-to-video generation
- Keyframe animation workflows

---

# Quick Start

## 1. Create an API Key

Get your API key from:

```text
https://platform.agnes-ai.com/
```

---

## 2. Configure Hermes

Set the required environment variables:

```bash
export AGNES_API_KEY="your_api_key"
export AGNES_BASE_URL="https://apihub.agnes-ai.com/v1"
```

For Token Plan:

```bash
export AGNES_TOKEN_PLAN_API_KEY="your_token_plan_key"
export AGNES_BASE_URL="https://apihub.agnes-ai.com/v1"
```

---

# Example Usage

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://apihub.agnes-ai.com/v1"
)

response = client.chat.completions.create(
    model="agnes-2.0-flash",
    messages=[
        {
            "role": "user",
            "content": "Explain how AI agents work."
        }
    ]
)

print(response.choices[0].message.content)
```

---

# Use Cases

Agnes AI can be used for:

- AI assistants
- Developer tools
- Coding platforms
- Agent automation systems
- Research applications
- Content creation platforms
- Image generation products
- Video generation applications
- Enterprise AI solutions

---

# Data Usage

Agnes AI provides different service tiers with different data usage practices.

- Free Services may use eligible interactions for product and model improvement where applicable.
- Paid Token Plan users are excluded from model training by default unless explicit authorization is provided.

Users should avoid submitting sensitive, confidential, or regulated information unless they have appropriate authorization and protections.

---

# Resources

Official Platform:

https://platform.agnes-ai.com/

API Documentation:

https://agnes-ai.com/en/docs/overview

Website:

https://agnes-ai.com/

---

# About Sapiens AI

Sapiens AI is the parent company behind Agnes AI, building advanced multimodal AI models and infrastructure.

Our mission is to make world-class AI accessible to everyone by enabling developers and organizations to integrate powerful AI capabilities into their products.

---

# License

This repository contains Hermes provider integrations for Agnes AI.

© Agnes AI / Sapiens AI
