

def get_minimal_representation(pos, ref, alt): 
	"""
	Get the minimal representation of a variant, based on the ref + alt alleles in a VCF
	This is used to make sure that multiallelic variants in different datasets, 
	with different combinations of alternate alleles, can always be matched directly. 

	Note that chromosome is ignored here - in xbrowse, we'll probably be dealing with 1D coordinates 
	Args: 
		pos (int): genomic position in a chromosome (1-based)
		ref (str): ref allele string
		alt (str): alt allele string
	Returns: 
		tuple: (pos, ref, alt) of remapped coordinate
	"""

	# If it's a simple SNV, don't remap anything
	if len(ref) == 1 and len(alt) == 1: 
		return pos, ref, alt

	# Add a bucch of elif clauses here... 
 