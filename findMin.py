def findMin(A,l,h):
	if A[l] <= A[h]:
		return A[l]

	mid = int((l+h)/2)
	return min([findMin(A,l,mid) , findMin(A,mid+1,h)])


