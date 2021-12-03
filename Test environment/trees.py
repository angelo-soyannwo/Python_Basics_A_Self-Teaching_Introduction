

def tree(root_label, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root_label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]
 

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True
	
def is_leaf(tree):
	if type(tree) == int:
		return True
	return not branches(tree)

def fib_tree(n):
	if n == 0 or n == 1:
		return tree(n)
	else:
		left, right = fib_tree(n-2), fib_tree(n-1)
		fib_n = str(n) + "th number in fib sequence"
		return tree(fib_n, [left, right])

def count_leaves(tree):
	k = 0
	if is_leaf(tree):
		return 1
	else:
		branch_counts = [count_leaves(b) for b in branches(tree)]
		print(branch_counts)
		
	return sum(branch_counts, 0) 



def partition_tree(n, m):
	"""Return a partion tree of n using numbers up to n"""
	if n == 0:
		return tree(True)
	elif n < 0 or m == 0:
		return tree(False)
	else:
		left, right = partition_tree(n-m, m), partition_tree(n, m-1)
		return tree(m, [left, right])

def print_parts(tree, partition=[]):
	if is_leaf(tree):
		if label(tree):
			print(" + ".join(partition))
	else:
		left, right = branches(tree)
		m = str(label(tree))
		print_parts(left, partition + [m])
		print_parts(right, partition)

def right_binarize(tree):
        """Construct a right-branching binary tree."""
        if is_leaf(tree):
            return tree
        if len(tree) > 2:
            tree = [tree[0], tree[1:]]
        return [right_binarize(b) for b in tree]

def main():
	print(fib_tree(5))
#	t = partition_tree(5, 3)
#	print(t)
#	print_parts(t)
#	print(right_binarize([1, 2, 3, 4, 5, 6, 7]))



if __name__ == "__main__":
	main()
