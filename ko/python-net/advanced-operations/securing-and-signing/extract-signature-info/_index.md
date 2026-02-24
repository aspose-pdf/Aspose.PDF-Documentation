---
title: 서명에서 세부 정보 추출
linktitle: 서명에서 세부 정보 추출
type: docs
weight: 20
url: /ko/python-net/extract-image-and-signature-information/
description: PDF 문서에서 디지털 서명의 이미지를 Aspose.PDF for Python을 사용하여 추출하는 방법.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 서명 세부 정보를 가져옵니다
Abstract: 이 문서에서는 Aspose.PDF for Python을 사용하여 PDF 문서에서 이미지와 디지털 서명 정보를 추출하는 방법을 보여줍니다. 포함된 이미지를 식별, 접근 및 저장하는 단계별 지침과 디지털 서명의 메타데이터 및 검증 상태를 검색하는 코드 샘플을 제공합니다.
---

## 서명 필드에서 이미지 추출

Aspose.PDF for Python via .NET은 [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) 클래스를 사용하여 PDF 파일에 디지털 서명을 하는 기능을 지원합니다.

이 코드 스니펫은 Aspose.PDF for Python을 사용하여 PDF 문서에서 디지털 서명 이미지를 추출하는 방법을 보여줍니다.

단계:

1. PDF 문서를 엽니다.
1. 양식 필드를 반복하여 SignatureField 객체를 찾습니다.
1. 각 서명에 연결된 이미지를 추출합니다(가능한 경우).
1. 추출한 서명 이미지를 JPEG 파일로 저장합니다.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue

            image_stream = signature_field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            # Save the image
            image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## 서명 정보 추출

Aspose.PDF for Python via .NET은 SignatureField 클래스를 사용하여 PDF 파일에 디지털 서명을 하는 기능을 지원합니다. 현재 우리는 인증서의 유효성을 확인할 수 있지만 전체 인증서를 추출할 수는 없습니다. 추출 가능한 정보는 공개키, 지문, 발행자 등입니다.

서명 정보를 추출하기 위해 [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) 메서드를 [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) 클래스에 도입했습니다. 다음 코드 스니펫을 살펴보면 SignatureField 객체에서 인증서를 추출하는 단계가 시연됩니다:

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue
            # Extract certificate
            certificate_stream = signature_field.extract_certificate()
            if certificate_stream is None:
                continue
            # Save certificate
            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                with open(path_outfile, "wb") as file_stream:
                    certificate_stream.read(bytes_data, 0, len(bytes_data))
                    file_stream.write(bytes_data)
```

문서 서명 알고리즘에 대한 정보를 얻을 수 있습니다.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            signatures_info_list = signature.get_signatures_info()
            for sig_info in signatures_info_list:
                print(sig_info.DIGEST_HASH_ALGORITHM)
                print(sig_info.ALGORITHM_TYPE)
                print(sig_info.CRYPTOGRAPHIC_STANDARD)
                    print(sig_info.signature_name)
```

## 서명 손상 검사

이 코드 스니펫은 Aspose.PDF for Python을 사용하여 PDF 문서에서 손상된 디지털 서명을 감지하는 방법을 보여줍니다.

단계는 다음과 같습니다:

1. PDF 문서를 엽니다.
1. 문서를 분석하기 위해 'SignaturesCompromiseDetector' 인스턴스를 생성합니다.
1. 손상된(무효이거나 변경된) 디지털 서명이 있는지 확인합니다.
1. 발견된 손상된 서명의 이름을 출력합니다.
1. 서명 적용 범위를 보고합니다—문서 중 얼마나 많은 부분이 유효한 서명으로 보호되는지를 나타냅니다.

이 기능은 법률, 금융 및 규정 준수 중심 환경처럼 문서의 진위와 무결성을 검증해야 하는 경우에 매우 중요합니다. 개발자가 서명된 PDF의 변조 또는 손상을 자동으로 감지할 수 있도록 합니다.

Aspose.PDF는 디지털 서명 검증을 위한 포괄적인 도구 세트를 제공하여, 문서 신뢰성을 유지하는 보안 서명 인식 애플리케이션을 보다 쉽게 구축할 수 있게 합니다.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create the compromise detector instance
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        # Check for compromise
        if detector.check(result):
            print("No signature compromise detected")
            return

        # Get information about compromised signatures
        if result[0].has_compromised_signatures:
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```

