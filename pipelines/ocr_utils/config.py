from dataclasses import dataclass

import yaml


@dataclass(frozen=True)
class AppConfig:
    vlm_api_url: str
    vlm_api_key: str
    vlm_model_name: str

    temperature: float
    presence_penalty: float
    repetition_penalty: float

    dpi: int

    openwebui_host: str
    openwebui_token: str

    @classmethod
    def from_yaml(cls, path: str = "pipelines/ocr_utils/config.yaml") -> "AppConfig":
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return cls(
            vlm_api_url=data["vlm_api_url"],
            vlm_api_key=data["vlm_api_key"],
            vlm_model_name=data["vlm_model_name"],
            temperature=data["temperature"],
            presence_penalty=data["presence_penalty"],
            repetition_penalty=data["repetition_penalty"],
            dpi=data["dpi"],
            openwebui_host=data["openwebui_host"],
            openwebui_token=data["openwebui_token"],
        )
