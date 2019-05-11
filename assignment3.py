#! /usr/bin/env python3

import importlib
import vcf
import httplib2

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
    
    def __init__(self):
        ''''
        check if pyvcf is installed and print version
        '''
        vcf_exists = importlib.util.find_spec("vcf")
        if vcf_exists:
            if "vcf" in dir():
                print("PyVCF version: %s" % vcf.VERSION)
            else:
                print("PyVCF installed but not imported.")
        else:
            print("ERROR! PyVCF not installed. "
                  "Run \n"
                  "$ pip3 install pyvcf \n"
                  "to install. ")
        

    def annotate_vcf_file(self):
        '''
        - Annotate the VCF file using the following example code (for 1 variant)
        - Iterate of the variants (use first 900)
        - Store the result in a data structure
        :return:
        '''    
        print("TODO")
        
        
        ##
        ## Example code for 1 variant
        ##
        # import httplib2
        h = httplib2.Http()
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        params = 'ids=chr16:g.28883241A>G,chr1:g.35367G>A'
        res, con = h.request('http://myvariant.info/v1/variant', 'POST', params, headers=headers)
        
        ## Use .decode('utf-8') on con object
        
        ##
        ## End example code
        ##
        
        return None  ## return the data structure here
    
    
    def get_list_of_genes(self):
        '''
        Print the name of genes in the annotation data set
        :return:
        '''
        print("TODO")
    
    
    def get_num_variants_modifier(self):
        '''
        Print the number of variants with putative_impact "MODIFIER"
        :return:
        '''
        print("TODO")
        
    
    def get_num_variants_with_mutationtaster_annotation(self):
        '''
        Print the number of variants with a 'mutationtaster' annotation
        :return:
        '''
        print("TODO")
        
    
    def get_num_variants_non_synonymous(self):
        '''
        Print the number of variants with 'consequence' 'NON_SYNONYMOUS'
        :return:
        '''
        print("TODO")
        
    
    def view_vcf_in_browser(self):
        '''
        - Open a browser and go to https://vcf.iobio.io/
        - Upload the VCF file and investigate the details
        :return:
        '''
   
        ## Document the final URL here
        print("TODO")
            
    
    def print_summary(self):
        print("Print all results here")
    
    
def main():
    print("Assignment 3")
    assignment3 = Assignment3()
    assignment3.print_summary()
    print("Done with assignment 3")
        
        
if __name__ == '__main__':
    main()
   
    



