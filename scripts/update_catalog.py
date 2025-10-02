#!/usr/bin/env python3
"""
Script to fetch available models from Regolo API and update catalog-v1.csv
"""
import os
import sys
import json
from typing import List
import urllib.request
import urllib.error


def fetch_models_from_api(api_key: str) -> List[str]:
    """
    Fetch the list of available models from Regolo API.
    
    Args:
        api_key: Regolo API key
        
    Returns:
        List of model names (IDs)
        
    Raises:
        Exception: If the API request fails
    """
    api_url = "https://api.regolo.ai/v1/models"
    
    headers = {
        "accept": "application/json",
        "X-Auth": api_key
    }
    
    req = urllib.request.Request(api_url, headers=headers, method="GET")
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status != 200:
                raise Exception(f"API returned status {response.status}")
            
            data = json.loads(response.read().decode('utf-8'))
            
            # The response should be an object with a 'data' array
            # Each item in 'data' has an 'id' field with the model name
            if not isinstance(data, dict) or 'data' not in data:
                raise Exception(f"Unexpected API response format: {data}")
            
            models = []
            for item in data['data']:
                if isinstance(item, dict) and 'id' in item:
                    models.append(item['id'])
            
            if not models:
                raise Exception("No models found in API response")
            
            return models
            
    except urllib.error.HTTPError as e:
        raise Exception(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise Exception(f"URL Error: {e.reason}")
    except json.JSONDecodeError as e:
        raise Exception(f"JSON decode error: {e}")


def write_catalog_csv(models: List[str], filepath: str = "catalog-v1.csv") -> None:
    """
    Write the models list to a CSV file (one model per line).
    
    Args:
        models: List of model names
        filepath: Path to the CSV file
    """
    # Sort models alphabetically for consistency
    models_sorted = sorted(models)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        for model in models_sorted:
            f.write(f"{model}\n")
    
    print(f"✓ Written {len(models_sorted)} models to {filepath}")


def main() -> int:
    """Main entry point."""
    api_key = os.getenv("REGOLO_API_KEY")
    
    if not api_key:
        print("Error: REGOLO_API_KEY environment variable not set", file=sys.stderr)
        return 1
    
    try:
        print("Fetching models from Regolo API...")
        models = fetch_models_from_api(api_key)
        print(f"✓ Fetched {len(models)} models")
        
        print("Updating catalog-v1.csv...")
        write_catalog_csv(models)
        
        print("✓ Catalog updated successfully")
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())


