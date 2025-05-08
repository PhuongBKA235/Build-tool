import os

# Danh sách file mẫu cần tạo
docs_structure = {
    "docs/business/BRD.md": "# Business Requirement Document\n\n## Mục tiêu\n\n## Đối tượng sử dụng\n\n## Yêu cầu nghiệp vụ...",
    "docs/business/FRD.md": "# Functional Requirement Document\n\n## Tính năng chính\n\n## Luồng hoạt động...",
    "docs/design/architecture.md": "# Kiến trúc hệ thống\n\n(Sơ đồ vẽ tay/ảnh nên đặt kèm trong thư mục này)",
    "docs/design/erd.md": "# ERD (Entity Relationship Diagram)\n\n(Mô tả cơ sở dữ liệu, các bảng và quan hệ)",
    "docs/design/api_spec.yaml": "openapi: 3.0.0\ninfo:\n  title: API Spec\n  version: 1.0.0\npaths:\n  /example:\n    get:\n      summary: Example API",
    "docs/dev/README.md": "# Hướng dẫn cài đặt\n\n## Cách chạy local\n\n## Cấu trúc thư mục",
    "docs/dev/deploy_guide.md": "# Hướng dẫn triển khai\n\n## Cấu hình môi trường\n\n## CI/CD",
    "docs/dev/changelog.md": "# Change Log\n\n## v1.0.0\n- Khởi tạo dự án",
    "docs/test/test_plan.md": "# Kế hoạch kiểm thử\n\n## Phạm vi\n\n## Loại test...",
    "docs/test/test_cases.md": "# Test Cases\n\n| Test | Input | Output | Result |\n|------|-------|--------|--------|"
}

# Tạo file và thư mục tương ứng
for path, content in docs_structure.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Đã tạo bộ khung tài liệu dự án tại thư mục ./docs")
