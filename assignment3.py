#! /usr/bin/env python3

import vcf
import httplib2
import json

__author__ = 'Lisa Schneider'


##
##
## Aim of this assignment is to annotate the variants with various attributes
## We will use the API provided by "myvariant.info" - more information here: https://docs.myvariant.info
## NOTE NOTE! - check here for hg38 - https://myvariant.info/faq
## 1) Annotate the first 900 variants in the VCF file
## 2) Store the result in a data structure (not in a database)
## 3) Use the data structure to answer the questions
##
## 4) View the VCF in a browser
##

class Assignment3:

    def __init__(self, in_vcf):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)

        ## Call annotate_vcf_file here
        self.vcf_path = in_vcf  # TODO
        self.annotation_data = self.annotate_vcf_file()

    def annotate_vcf_file(self):
        '''
        - Annotate the VCF file using the following example code (for 1 variant)
        - Iterate of the variants (use first 900)
        - Store the result in a data structure
        :return: annotation data
        '''
        ## Build the connection
        h = httplib2.Http()
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        params_pos = []  # List of variant positions
        with open(self.vcf_path) as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for counter, record in enumerate(vcf_reader):
                params_pos.append(record.CHROM + ":g." + str(record.POS) + record.REF + ">" + str(record.ALT[0]))

                if counter >= 899:
                    break

        ## Build the parameters using the list we just built
        params = 'ids=' + ",".join(params_pos) + '&hg38=true'

        ## Perform annotation
        res, con = h.request('http://myvariant.info/v1/variant', 'POST', params, headers=headers)
        annotation_result = con.decode('utf-8')

        annotation_dataset = json.loads(annotation_result)

        return annotation_dataset

    def get_list_of_genes(self, annotation_data):
        '''
        Print the name of genes in the annotation data set
        :return: Nothing
        '''
        gene_list = []
        for line in annotation_data:
            if 'cadd' in line:
                if 'genename' in line['cadd']['gene']:
                    gene_list.append(line['cadd']['gene']['genename'])
        gene_string = ', '.join(gene_list)
        print(f"List of genes: \n"
              f"\t{gene_string}")

    def get_num_variants_modifier(self, annotation_data):
        '''
        Print the number of variants with putative_impact "MODIFIER"
        :return: Nothing
        '''
        counter = 0
        for line in annotation_data:
            if "snpeff" in line:
                if "putative_impact" in line['snpeff']['ann']:
                    if line['snpeff']['ann']['putative_impact'] == 'MODIFIER':
                        counter += 1
        print("Number of variants with putative impact 'MODIFIER': ", counter)

    def get_num_variants_with_mutationtaster_annotation(self, annotation_data):
        '''
        Print the number of variants with a 'mutationtaster' annotation_data
        :return: Nothing
        '''
        counter = 0
        for line in annotation_data:
            if 'dbnsfp' in line:
                if 'mutationtaster' in line['dbnsfp']:
                    counter += 1
        print(f"Number of variants with mutationtaster annotation_data: {counter}")

    def get_num_variants_non_synonymous(self, annotation_data):
        '''
        Print the number of variants with 'consequence' 'NON_SYNONYMOUS'
        :return: Nothing
        '''
        counter = 0
        for line in annotation_data:
            if 'cadd' in line:
                if 'consequence' in line['cadd']:
                    if line['cadd']['consequence'] == "NON_SYNONYMOUS":
                        counter += 1
        print(f"Number of non synonymous variants: {counter}")

    def view_vcf_in_browser(self):  
        '''
        - Open a browser and go to https://vcf.iobio.io/
        - Upload the VCF file and investigate the details
        :return: Nothing
        '''
        ## Document the final URL here
        print("The vcf file was compressed and indexed and the results were visualized with the vcf.iobio website.\n" 
              "\t https://vcf.iobio.io/?species=Human&build=GRCh38\n"
              "Upload a .tar.gz and a .tar.gz.tbi archive of your vcf-File")


    def print_summary(self):
        # dataset = self.annotate_vcf_file()
        print("Print all results here")
        self.get_list_of_genes(self.annotation_data)
        self.get_num_variants_modifier(self.annotation_data)
        self.get_num_variants_with_mutationtaster_annotation(self.annotation_data)
        self.get_num_variants_non_synonymous(self.annotation_data)
        self.view_vcf_in_browser()


def main():
    print("Assignment 3")
    assignment3 = Assignment3("chr16.vcf")
    assignment3.print_summary()
    print("Done with assignment 3")


if __name__ == '__main__':
    main()




