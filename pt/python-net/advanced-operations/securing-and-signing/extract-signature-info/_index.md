---
title: Extrair detalhes da assinatura
linktitle: Extrair detalhes da assinatura
type: docs
weight: 20
url: /pt/python-net/extract-image-and-signature-information/
description: Como extrair imagem de assinatura digital em documentos PDF usando Aspose.PDF para Python.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenha detalhes da assinatura em PDFs usando Python
Abstract: Este artigo demonstra como extrair imagens e informações de assinaturas digitais de documentos PDF usando Aspose.PDF para Python. Ele fornece instruções passo a passo e exemplos de código para identificar, acessar e salvar imagens incorporadas, bem como recuperar metadados e o status de validação das assinaturas digitais.
---

## Extraindo Imagem do Campo de Assinatura

Aspose.PDF for Python via .NET suporta o recurso de assinar digitalmente os arquivos PDF usando a classe [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) .

Este trecho de código demonstra como extrair imagens de assinaturas digitais de um documento PDF usando Aspose.PDF para Python.

Passos:

1. Abrindo o documento PDF.
1. Iterando pelos campos do formulário para localizar quaisquer objetos SignatureField.
1. Extraindo a imagem associada a cada assinatura (se disponível).
1. Salvando a imagem de assinatura extraída como um arquivo JPEG.

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

## Extrair Informações da Assinatura

Aspose.PDF for Python via .NET suporta o recurso de assinar digitalmente os arquivos PDF usando a classe SignatureField. Atualmente, também podemos determinar a validade do certificado, mas não podemos extrair o certificado completo. As informações que podem ser extraídas são a chave pública, impressão digital, emissor, etc.

Para extrair informações da assinatura, introduzimos o método [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) na classe [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) . Por favor, confira o trecho de código a seguir que demonstra os passos para extrair o certificado do objeto SignatureField:

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

Você pode obter informações sobre os algoritmos de assinatura do documento.

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

## Verificando comprometimento de assinaturas

Este trecho de código demonstra como detectar assinaturas digitais comprometidas em um documento PDF usando Aspose.PDF para Python.

Os passos incluem:

1. Abrindo o documento PDF.
1. Criando uma instância de 'SignaturesCompromiseDetector' para analisar o documento.
1. Verificando se há assinaturas digitais comprometidas (inválidas ou alteradas).
1. Imprimindo os nomes de quaisquer assinaturas comprometidas encontradas.
1. Relatando a cobertura de assinatura — indicando quanto do documento está protegido por assinaturas válidas.

Este recurso é crítico em casos de uso onde a autenticidade e integridade do documento devem ser verificadas, como em ambientes jurídicos, financeiros e de conformidade. Ele permite que desenvolvedores detectem automaticamente adulterações ou corrupção de PDFs assinados.

Aspose.PDF oferece um conjunto abrangente de ferramentas para validação de assinaturas digitais, facilitando a construção de aplicações seguras e conscientes de assinaturas que preservam a confiabilidade dos documentos.

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

