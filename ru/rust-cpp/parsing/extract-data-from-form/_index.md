---
title: Извлечь данные из AcroForm с помощью Rust
linktitle: Извлечь данные из AcroForm
type: docs
weight: 50
url: /ru/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF делает процесс извлечения данных полей формы из PDF-файлов простым. Узнайте, как извлечь данные из AcroForms и сохранить их в формат XML, FDF или XFDF.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из AcroForm с помощью Rust
Abstract: В этой статье объясняется, как извлекать данные AcroForm из PDF‑файлов с помощью Aspose.PDF for Rust via C++ и экспортировать их в широко используемые форматы обмена данными — XML, FDF и XFDF. Показано, как открыть PDF‑документ, содержащий интерактивные поля формы, и программно экспортировать имена полей формы и их значения для повторного использования за пределами исходного PDF. Предоставляя практические примеры на Rust для каждого формата экспорта, статья освещает типичные рабочие процессы, включая обработку данных, отправку форм, интеграцию систем и долговременное хранение данных, помогая разработчикам эффективно управлять и повторно использовать данные форм PDF в своих приложениях.
---

## Экспорт данных в XML из PDF‑файла

Этот фрагмент кода показывает, как экспортировать данные AcroForm из PDF‑документа в файл XML с использованием Aspose.PDF for Rust.
Процесс включает открытие существующего PDF‑файла с полями формы, затем экспорт этих полей и их значений в XML‑документ для дальнейшей обработки, хранения или обмена данными.

1. Откройте PDF‑документ.
1. Вызовите метод 'export_xml' для извлечения данных полей формы и сохранения их в виде XML‑файла.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## Экспортировать данные в FDF из PDF-файла

Aspose.PDF for Rust via C++ позволяет экспортировать данные AcroForm из PDF‑документа в файл FDF. Файл Формат Данных Форм (FDF) хранит имена полей формы и их значения отдельно от PDF, что делает его полезным для обмена данными, процессов отправки форм и архивирования данных форм без внедрения их в исходный документ.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## Экспорт данных в XFDF из PDF‑файла

XFDF (XML Forms Data Format) — это формат на основе XML, который представляет данные полей формы отдельно от PDF‑файла, что делает его идеальным для обмена данными, отправки форм и интеграции с веб‑ориентированными рабочими процессами.
Aspose.PDF for Rust via C++ помогает экспортировать данные AcroForm из PDF‑документа в файл XFDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```
