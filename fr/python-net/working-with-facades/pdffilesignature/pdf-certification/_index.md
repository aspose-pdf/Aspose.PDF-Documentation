---
title: Certification PDF
type: docs
weight: 30
url: /fr/python-net/pdf-certification/
description: Apprenez à certifier des documents PDF en Python à l'aide de PdfFileSignature et DocMDPSignature avec différentes autorisations de modification du document.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certifier des documents PDF avec les autorisations DocMDP en Python
Abstract: Cet article explique comment certifier des documents PDF avec Aspose.PDF for Python via .NET en utilisant la façade PdfFileSignature. Il montre comment créer une DocMDPSignature, appliquer une certification avec des autorisations de remplissage de formulaire, et verrouiller un document avec un niveau de certification sans modifications.
---

Aspose.PDF for Python via .NET vous permet de certifier des documents PDF en appliquant une signature au niveau du document avec [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/). La certification est différente d'une signature d'approbation standard car elle définit les modifications, le cas échéant, autorisées après que le document a été certifié.

Cet article présente deux flux de travail de certification courants :

1. Certifier un PDF et autoriser le remplissage de formulaire après la certification.
1. Certifier un PDF et empêcher toute modification ultérieure.

## Certifier un PDF pour le remplissage de formulaire

Utilisez cette approche lorsque le document doit rester certifié mais que les utilisateurs doivent toujours remplir des formulaires interactifs ou continuer à signer le fichier. Le `FILLING_IN_FORMS` Le niveau d\u0027autorisation permet ces modifications contrôlées tout en maintenant la certification valide.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def certify_pdf_with_mdp_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Appliquer une certification au niveau du document sans autoriser de modifications

Utilisez ce mode lorsque le document certifié doit rester inchangé après la certification. Le `NO_CHANGES` Le niveau d'autorisation convient aux PDF finalisés où toute modification ultérieure doit invalider l'état de certification.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_document_level_certification(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
