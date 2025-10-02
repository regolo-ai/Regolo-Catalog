# Regolo Model Catalog

This repository contains the official catalog of available models on the Regolo AI platform.

## 📋 Overview

The catalog is automatically updated every 24 hours by fetching the latest list of available models from the Regolo API. This ensures that all applications using Regolo models always have access to the most up-to-date model list.


## 🔄 Automatic Updates

The catalog is automatically updated daily at **2:00 AM UTC** via a GitHub Action that:

1. Calls the Regolo API endpoint: `GET https://api.regolo.ai/v1/models`
2. Extracts the model names from the response
3. Updates `catalog-v1.csv` with the current model list
4. Commits and pushes changes (only if there are modifications)

The GitHub Action can also be triggered manually from the Actions tab.

## 🌐 Consuming the Catalog

### Raw URL

You can access the catalog directly via the GitHub raw URL:

```
https://raw.githubusercontent.com/regolo-ai/Regolo-Catalog/main/catalog-v1.csv
```

### Python Example

```python
import urllib.request
import csv

CATALOG_URL = "https://raw.githubusercontent.com/regolo-ai/Regolo-Catalog/main/catalog-v1.csv"

def load_models():
    with urllib.request.urlopen(CATALOG_URL) as response:
        content = response.read().decode('utf-8')
        models = [line.strip() for line in content.split('\n') if line.strip()]
    return models

models = load_models()
print(f"Available models: {models}")
```

### JavaScript Example

```javascript
const CATALOG_URL = "https://raw.githubusercontent.com/regolo-ai/Regolo-Catalog/main/catalog-v1.csv";

async function loadModels() {
  const response = await fetch(CATALOG_URL);
  const text = await response.text();
  const models = text.trim().split('\n').filter(line => line.trim());
  return models;
}

const models = await loadModels();
console.log('Available models:', models);
```

## 📊 Update Schedule

- **Daily update**: 2:00 AM UTC
- **Recommended fetch time**: 3:00 AM UTC or later

## 🤝 Request a Model

Want to see a specific model on Regolo? Let us know! You can:
- Open an [issue](https://github.com/regolo-ai/Regolo-Catalog/issues)
- Start a [discussion](https://github.com/regolo-ai/Regolo-Catalog/discussions)
- Contact us at support@regolo.ai

## 📝 License

MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [Regolo Observe](https://github.com/regolo-ai/regoloobserve) - Observability platform for Regolo models
