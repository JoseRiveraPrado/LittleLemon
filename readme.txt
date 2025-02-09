/api-token-auth/            # Token authentication via DRF
/menu/                      # GET: List menu items / POST: Create item (requires authentication)
/menu/<id>/                 # GET: Retrieve an item / PUT: Update / DELETE: Remove (requires authentication)
/restaurant/booking/        # GET: List bookings / POST: Create booking (requires authentication)
/restaurant/booking/<id>/   # GET, PUT, DELETE specific bookings