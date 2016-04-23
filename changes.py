def group_activity(request):
	input_dict = json.loads(request.body)
	op = int(input_dict["op"])
	#0 - create group
	## TODO -polling if already part of group in this intent
	#1 - view members
	#2 - group chat
	#3 - exit group
	if op==0:
		phone = input_dict["phone"]
		gname = input_dict["gname"]
		gdest = input_dict["gdest"]
		members = input_dict["members"][1:-1].split(",")
		#data = request.body[1:-1].split(",")
		group = Group.objects.create(name=gname,destination=gdest)
		user = User.objects.get(phone_number=phone)
		UserIsGroupMember.objects.create(g_id=group,phone_number=user)
		UserIsAdminGroup.objects.create(g_id=group,phone_number=user)
		for member in members:
			try:
				UserIsGroupMember.objects.create(g_id=group,phone_number=member)
		##TODO return ?(locations of users to plot on map)?
		return HttpResponse("Success")
		
		
	if op==1:
		phone = input_dict["phone"]
		g_id = UserIsGroupMember.objects.get(phone_number=user1).g_id.g_id
		group = Group.objects.get(g_id=g_id)
		members = UserIsGroupMember.objects.filter(g_id=group)
		phones=[]
		names=[]
		for member in members:
			phones.append(member.phone_number.phone_number)
			names.append(member.phone_number.name)
		json_response = {}
		json_response["member_names"] = ";".join(names)
		json_response["member_phones"] = ";".join(phones)
		return HttpResponse(json.dumps(json_response))
	if op==2:
		
	if op==3:
		phone = input_dict["phone"]
\		try:
			g_id = UserIsGroupMember.objects.get(phone_number=user1).g_id.g_id
			group = Group.objects.get(g_id=g_id)
			group.delete()
			return HttpResponse("Success")

			