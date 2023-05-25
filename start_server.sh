/home/guru/.local/bin/uvicorn api:app --reload | awk '{ print strftime(), $0; fflush() }' >> log.log
