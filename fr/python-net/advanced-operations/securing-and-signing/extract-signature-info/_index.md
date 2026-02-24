---
title: Extraire les détails de la signature
linktitle: Extraire les détails de la signature
type: docs
weight: 20
url: /fr/python-net/extract-image-and-signature-information/
description: Comment extraire l'image d'une signature numérique dans les documents PDF à l'aide d'Aspose.PDF pour Python.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenez les détails de la signature dans les PDF avec Python
Abstract: Cet article montre comment extraire les images et les informations de signature numérique des documents PDF à l'aide d'Aspose.PDF pour Python. Il fournit des instructions étape par étape et des exemples de code pour identifier, accéder et enregistrer les images intégrées, ainsi que pour récupérer les métadonnées et le statut de validation des signatures numériques.
---

## Extraction d'image du champ de signature

Aspose.PDF pour Python via .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/).

Cet extrait de code montre comment extraire les images des signatures numériques d'un document PDF à l'aide d'Aspose.PDF pour Python.

Étapes :

1. Ouverture du document PDF.
1. Parcourir les champs de formulaire pour localiser les objets SignatureField.
1. Extraire l'image associée à chaque signature (si disponible).
1. Enregistrer l'image de signature extraite sous forme de fichier JPEG.

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

## Extraire les informations de la signature

Aspose.PDF pour Python via .NET prend en charge la fonctionnalité de signature numérique des fichiers PDF en utilisant la classe SignatureField. Actuellement, nous pouvons également déterminer la validité du certificat mais nous ne pouvons pas extraire le certificat complet. Les informations pouvant être extraites sont une clé publique, l'empreinte digitale, l'émetteur, etc.

Pour extraire les informations de signature, nous avons ajouté la méthode [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) à la classe [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Veuillez consulter l'extrait de code suivant qui montre les étapes pour extraire le certificat de l'objet SignatureField :

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

Vous pouvez obtenir des informations sur les algorithmes de signature du document.

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

## Vérification des signatures compromises

Cet extrait de code montre comment détecter les signatures numériques compromises dans un document PDF à l'aide d'Aspose.PDF pour Python.

Les étapes comprennent :

1. Ouverture du document PDF.
1. Création d'une instance 'SignaturesCompromiseDetector' pour analyser le document.
1. Vérification de toute signature numérique compromise (invalide ou modifiée).
1. Affichage des noms des signatures compromises trouvées.
1. Rapport sur la couverture des signatures — indiquant quelle partie du document est protégée par des signatures valides.

Cette fonctionnalité est cruciale dans les cas d'utilisation où l'authenticité et l'intégrité du document doivent être vérifiées, comme dans les environnements juridiques, financiers et de conformité. Elle permet aux développeurs de détecter automatiquement toute altération ou corruption des PDF signés.

Aspose.PDF propose un ensemble complet d'outils pour la validation des signatures numériques, facilitant la création d'applications sécurisées et conscientes des signatures qui garantissent la fiabilité des documents.

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

