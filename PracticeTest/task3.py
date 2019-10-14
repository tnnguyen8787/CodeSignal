
n(arr):
	    sum = 0
		    for ele in arr:
				        sum += ele
						        
								    return sum/len(arr)


								def meanGroups(a):
									    meanGroups = [[]] *len(a)
										    meanDict = dict() # 'key' = mean : value index
											    if len(a) == 0:
													        return []
														    
														    else:
																        _mean = 0
																		        index_dict = 0
																				        for i,arr in enumerate(a):
																							            _mean = mean(arr)
																										            # if not in the dict add the man
																													            if _mean not in meanDict:
																																	                meanGroups[index_dict] = i
																																					                meanDict[_mean] = index_dict
																																									                index_dict +=1
																																													                
																																																	           
																																																			               else:
																																																							                   # if in the dict lookup 
																																																											                   meanGroups[meanDict[_mean]].append(i)
