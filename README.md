# Regolo Model Catalog

This repository contains the official catalog of available models on the Regolo AI platform.

## 📋 Overview

The catalog is automatically updated every 24 hours by fetching the latest list of available models from the Regolo API. This ensures that all applications using Regolo models always have access to the most up-to-date model list.

## 📁 Files

### `catalog-v1.csv`

The main catalog file containing the list of available models. Format:
- Plain CSV file
- One model name per line
- Models are sorted alphabetically
- No header row

**Example:**
```
deepseek-r1-70b
gemma-3-27b-it
gpt-oss-120b
Llama-3.1-8B-Instruct
...
```

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

## 🔒 API Key

The GitHub Action uses a `REGOLO_API_KEY` secret to authenticate with the Regolo API. This secret is configured in the repository settings and is not exposed in the workflow logs.

## 📊 Update Schedule

- **Catalog Update**: 2:00 AM UTC daily
- **Recommended Fetch Time**: 3:00 AM UTC or later (to ensure the latest catalog is available)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [Regolo Observe](https://github.com/regolo-ai/regoloobserve) - Observability platform for Regolo models

## 📧 Support

For issues or questions, please open an issue in this repository or contact support@regolo.ai.


