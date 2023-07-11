# MeSH therapeutic use based on chemical structure

Drug function, defined as Medical Subject Headings (MeSH) “therapeutic use” is predicted based on the chemical structure. 6955 non-redundant molecules, pertaining to one of the twelve therapeutic use classes selected, were downloaded from PubChem and used to train a binary classifier. The model provides the probability that a molecule has one of the following therapeutic uses: antineoplastic, cardiovascular, central nervous system (CNS), anti-infective, gastrointestinal, anti-inflammatory, dermatological, hematologic, lipid regulating, reproductive control, respiratory system, urological.

## Identifiers

* EOS model ID: `eos238c`
* Slug: `mesh-therapeutic-use`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Probability that the molecule belongs to each therapeutic use specified.

## References

* [Publication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6819987/)
* [Source Code](https://github.com/jgmeyerucsd/drug-class)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos238c)

## Citation

If you use this model, please cite the [original authors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6819987/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!