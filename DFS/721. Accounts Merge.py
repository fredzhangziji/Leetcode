import collections

class Solution(object):
    def accountsMerge(self, accounts):
        # Mapping email and name.
        email_to_name = {}
        # Mapping email and email (connected components).
        graph = collections.defaultdict(set)

        # Building the connected graph.
        for acc in accounts:
            cur_name = acc[0]
            for email in acc[1:]:
                # Map the email to the name, so that at last we know which name the connected
                # components belong to.
                email_to_name[email] = cur_name
                # Connect every email to the first email.
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                
        seen = set()
        res = []
        
        # Check the connected components.
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                components = []
                while stack:
                    node = stack.pop()
                    components.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            stack.append(neighbor)
                
                # After the stack is empty, we found the one entire connected componets,
                # and we add it to the answer.

                res.append([email_to_name[email]] +sorted(components))  
                                                  
        return res
                    