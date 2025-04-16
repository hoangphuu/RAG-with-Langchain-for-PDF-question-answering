import os
import wget
import urllib.parse
from typing import List, Dict
import logging
import string

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sanitize_filename(title: str) -> str:
    """Chuẩn hóa tên file để đảm bảo không có ký tự đặc biệt"""
    # Thay thế khoảng trắng bằng dấu gạch dưới
    title = title.replace(' ', '_')
    # Loại bỏ các ký tự không hợp lệ
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized = ''.join(c if c in valid_chars else '_' for c in title)
    return sanitized

def download_paper(file_link: Dict[str, str]) -> None:
    """Tải một bài báo từ ArXiv và lưu vào thư mục hiện tại"""
    try:
        # Chuẩn hóa URL
        url = file_link.get('url', '').strip()
        if not url:
            logger.error(f"URL không hợp lệ cho bài báo: {file_link.get('title', '')}")
            return

        # Chuẩn hóa tên file
        title = file_link.get('title', '')
        if not title:
            logger.error(f"Không tìm thấy tên bài báo trong: {file_link}")
            return

        sanitized_title = sanitize_filename(title)
        output_path = f"./{sanitized_title}.pdf"

        # Kiểm tra xem file đã tồn tại chưa
        if os.path.exists(output_path):
            logger.info(f"File đã tồn tại: {output_path}")
            return

        # Tải file
        logger.info(f"Đang tải: {title}")
        wget.download(url, out=output_path)
        logger.info(f"Đã tải xong: {output_path}")

    except Exception as e:
        logger.error(f"Lỗi khi tải bài báo {title}: {str(e)}")

# Danh sách các bài báo cần tải
def download_papers() -> None:
    """Tải tất cả các bài báo từ danh sách"""
    file_links = [
        {
            "title": "Attention Is All You Need",
            "url": "https://arxiv.org/pdf/1706.03762"
        },
        {
            "title": "BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding",
            "url": "https://arxiv.org/pdf/1810.04805"
        },
        {
            "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2201.11903"
        },
        {
            "title": "Denoising Diffusion Probabilistic Models",
            "url": "https://arxiv.org/pdf/2006.11239"
        },
        {
            "title": "Instruction Tuning for Large Language Models - A Survey",
            "url": "https://arxiv.org/pdf/2308.10792"
        },
        {
            "title": "Llama 2- Open Foundation and Fine-Tuned Chat Models",
            "url": "https://arxiv.org/pdf/2307.09288"
        }
    ]

    for file_link in file_links:
        download_paper(file_link)

if __name__ == "__main__":
    download_papers()